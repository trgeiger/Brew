"""empty message

Revision ID: 79085fc92590
Revises: 143c2c83997c
Create Date: 2016-09-02 14:30:14.267507

"""

# revision identifiers, used by Alembic.
revision = '79085fc92590'
down_revision = '143c2c83997c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brewlogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('origin', sa.String(length=64), nullable=True),
    sa.Column('method', sa.String(length=64), nullable=True),
    sa.Column('grind', sa.String(length=64), nullable=True),
    sa.Column('water', sa.Integer(), nullable=True),
    sa.Column('coffee', sa.Integer(), nullable=True),
    sa.Column('temp', sa.Integer(), nullable=True),
    sa.Column('flavor', sa.Text(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_brewlogs_method'), 'brewlogs', ['method'], unique=False)
    op.create_index(op.f('ix_brewlogs_origin'), 'brewlogs', ['origin'], unique=False)
    op.create_index(op.f('ix_brewlogs_timestamp'), 'brewlogs', ['timestamp'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_brewlogs_timestamp'), table_name='brewlogs')
    op.drop_index(op.f('ix_brewlogs_origin'), table_name='brewlogs')
    op.drop_index(op.f('ix_brewlogs_method'), table_name='brewlogs')
    op.drop_table('brewlogs')
    ### end Alembic commands ###