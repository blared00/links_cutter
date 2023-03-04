"""Init

Revision ID: d888860805eb
Revises: 
Create Date: 2023-03-05 00:56:10.175119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd888860805eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_link', sa.String(), nullable=True),
    sa.Column('short_link', sa.String(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_links_full_link'), 'links', ['full_link'], unique=True)
    op.create_index(op.f('ix_links_id'), 'links', ['id'], unique=False)
    op.create_index(op.f('ix_links_short_link'), 'links', ['short_link'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_links_short_link'), table_name='links')
    op.drop_index(op.f('ix_links_id'), table_name='links')
    op.drop_index(op.f('ix_links_full_link'), table_name='links')
    op.drop_table('links')
    # ### end Alembic commands ###
